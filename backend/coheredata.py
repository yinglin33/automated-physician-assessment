from urllib import response
import cohere

from cohere.classify import Example
co = cohere.Client("oPuYqWWEQLhzQ4U3wVj3fVYpqqZ8qN0vOIsUh8Fo")

overall_inputs = [
    "Why have you not visited the doctor earlier? Your condition is called Haemophilia, I will let the nurse discuss the procedure and the cost of the treatment. There is nothing to worry about.", 
    "You have suffered from an apoplexy, we will start the treatment right away, there is really nothing to worry about. I just need you to take a couple more tests and you should be good to go. What are the questions you have?",
    "How long have you been feeling these symptoms? Has it been longer than 2 days? Abetalipoproteinemia is an inherited disorder that impairs the normal absorption of fats and certain vitamins from the diet. Many of the signs and symptoms of abetalipoproteinemia result from a severe shortage (deficiency) of fat-soluble vitamins (vitamins A, E, and K). Also, how is the severity of the pain?", 
    "Oh why do you feel that way? Irritable bowel syndrome (IBS) is a common disorder that affects the stomach and intestines, also called the gastrointestinal tract, which explains the symptoms you are experiencing."
]

first_input = []
second_input = []
for paragraph in overall_inputs:
    s = ""
    a = ""
    temp = ""
    for c in paragraph:
        if c == "?":
            temp+="?"
            s+=temp
            temp = ""
        elif c == ".":
            temp+="."
            a+=temp
            temp = ""
        else:
            temp+=c
    first_input.append(a)
    second_input.append(s)


print(first_input)
print(second_input)
# (string, string) -> (int, arr : List[String])
def nlp(inputb, inputa):
    # B2, B4
    responseB = co.classify(
    model='large',
    inputs= [inputb],
    examples=[Example("Your Rough Endoplasmic Reticulum is not functioning as efficiently as it should. That is the root cause of the issue, we have a bunch of treatment options that could potentially help circumvent the issue.", "B2"), Example("We would have to perform a mini surgery on your upper aorta. Your left ventricular chamber is functioning well though. But we should get everything checked to ensure you are fine.", "B2"), Example("You will require kidney dialysis procedure for the next few months. After this procedure, if there is any progress, we will change the treatment accordingly. ", "B2"), Example("I have taken a look at your ECG, and we suspect that you have a condition known as heart arrhythmia. While this is a serious condition, we assure you that there is plenty of treatments available for you. ", "B2"), Example("For this condition, you have to take this barium meal. The barium meal helps create contrast in the scan, and we can get a better idea of what the condition is with a clearer scan.", "B4"), Example("You are suffering from this condition called haemophilia. This is a disorder in which blood doesn\'t clot normally. When blood can\'t clot properly, excessive bleeding, both external and internal, occurs after any injury or damage.", "B4"), Example("Based on the test results, you have a tear in your anterior labrum on your left shoulder, which means that the likelihood of your shoulder dislocating is significantly higher, especially when you stretch your shoulder in this particular way.", "B4"), Example("Based on the X-Ray, you are diagnosed with a hairline fracture. In other words, this means that you would need to immobilise your arm for the next 5-6 months for your bones to heal and regrow.", "B4"), Example("I have taken a look at your ECG, and we suspect that you have a condition known as heart arrhythmia, which is another way of saying you have irregular heart beats. There are a few treatment options for this that I will go over now. ", "B4"), Example("For this condition, you have to take this barium meal right before the scan. Once we get an accurate scan, we will give you further diagnosis.", "B2")]) 

    # A1, A3, A5
    responseA = co.classify(
    model='large',
    inputs=[inputa],
    examples=[Example("Do you feel like you have stomach pain? Why do you think you feel these emotions?", "A1"), Example("You’ve never had anything like this before? ", "A1"), Example("Does the pain feel like an ache? ", "A1"), Example("Is it a stabbing pain?", "A1"), Example("Is it a dull pain? ", "A1"), Example("That healed okay?", "A1"), Example("Why do you have cancer? Why is this the case?", "A1"), Example("Why haven’t you eaten gluten?", "A1"), Example("Why are you so paranoid about everything?", "A1"), Example("Do you think it is worth being this paranoid about your condition?", "A1"), Example("You don’t want to quit smoking now? Also, how is the severity of the pain?", "A3"), Example("Hey how are you doing? Do you feel good today?", "A3"), Example("How is your family doing? Do you have financial struggles that prevent you from getting the medical care you need? Do you feel you require more medical attention?", "A3"), Example("How would you describe the pain: how bad is it?", "A3"), Example("Do you use any alcohol, tobacco, or illicit drugs? ", "A3"), Example("Why do you think you might feel that way as you have described earlier?", "A3"), Example("Have you been feeling Better the past few days since the treatment last week?", "A3"), Example("How are you feeling today?", "A5"), Example("Do you smoke?", "A5"), Example("Tell me about your problem.", "A5"), Example("Tell me about the pain.", "A5"), Example("How would you describe the pain?", "A5"), Example("Does this burning sensation last long?", "A5"), Example("Is it a deep pain?", "A5"), Example("Does the pain seem to travel around?", "A5"), Example("What makes the pain feel worse? ", "A5"), Example("Is there anything else I can do to assist you further?", "A5"), Example("Why have you been feeling pain?", "A1")]) 
    
    statements = []
    output = 0
    if responseB.classifications[0].prediction == "B2":
        statements.append("The interviewer used difficult medical terms and jargon throughout the interview.")
        output += 2
    elif responseB.classifications[0].prediction == "B4":
        statements.append("The interviewer asked questions and provided information during the interview in language which was easily understood. The content of the interview was free of difficult medical terms and jargon. Jargon was immediately defined for the patient. Language used was appropriate to the patient’s level of education.")
        output+=4

    if responseA.classifications[0].prediction == "A1":
        statements.append("The interviewer failed to begin each line of questioning with open-ended questions. The interviewer asked many why, multiple or leading questions.")
        output+=1
    elif responseA.classifications[0].prediction == "A3":
        statements.append("The interviewer began the information gathering in most major lines of questioning with specific or direct questions OR the interviewer used 2 or more leading, why or multiple questions.")
        output+=3
    else:
        output+=5
        statements.append("The interviewer began the information gathering with an open- ended question which was followed up with more specific or direct questions. Each major line of questioning was begun with an open ended question; No poor questions were asked.")
    return (output, statements)



# i is a string
# frist_input is an array of str
overall_output = []
for count, i in enumerate(first_input):
    answer = nlp(i, second_input[count])
    overall_output.append(answer)

# [[score, [first feedback], [second feedback]].................]
print(overall_output)
    
    