'''
Created by Anuj Mishra on 21/08/2023

this is the file for langchain integration in this file i have used langcain with the gpt-3.5-turbo model to translate the text
to run the code and want to convert the json material kindly do uncomment the main funcion i/o content and replace the api key with 
the openai api key

Example input for this is
{
  "Title": "Photosynthesis",
  "Introduction": {
    "point": "Photosynthesis is a vital biological process that occurs in plants, algae, and some bacteria. It involves the conversion of light energy into chemical energy in the form of glucose and other organic compounds. This process is responsible for producing oxygen, which is essential for supporting life on Earth.",
    "img": "http://www.biology.arizona.edu/biochemistry/problem_sets/intro_photosynthesis/graphics/PSN-Reaction.jpg"
  },
  "History": {
    "point": "The process of photosynthesis was first studied by Jan Ingenhousz in the late 18th century. He discovered that plants release oxygen during the day in the presence of light. In the early 19th century, researchers like Julius von Sachs and Theodor Engelmann further advanced the understanding of photosynthesis. However, it was not until the mid-20th century that the complete mechanism of photosynthesis was elucidated.",
    "img": null
  },
  "Working Principle": {
    "point": "Photosynthesis occurs mainly in the chloroplasts of plant cells. The process can be divided into two stages: the light-dependent reactions and the light-independent reactions (Calvin cycle). In the light-dependent reactions, light energy is absorbed by chlorophyll and other pigments, leading to the generation of ATP and NADPH. These energy carriers are then used in the Calvin cycle to convert carbon dioxide into glucose.",
    "img": "https://i1.rgstatic.net/publication/229062430_Principles_of_photosynthesis/links/6040afd3299bf1e078549aeb/largepreview.png"
  },
  "Proof of Law": {
    "point": "Photosynthesis follows several fundamental principles:\n\n1. The Law of Conservation of Energy applies to photosynthesis. The total energy in the system before and after the process remains constant.\n2. The rate of photosynthesis is influenced by factors like light intensity, carbon dioxide concentration, and temperature.\n3. The overall equation for photosynthesis is: 6 CO2 + 6 H2O + light energy → C6H12O6 + 6 O2",
    "img": "https://i.ytimg.com/vi/2a8FyieAYH4/maxresdefault.jpg"
  },
  "Advantages": {
    "point": "Photosynthesis plays a critical role in maintaining the Earth's ecosystem. It produces oxygen, which is essential for respiration and the survival of many organisms. Additionally, photosynthesis is the foundation of the food chain, as it provides energy-rich organic molecules that sustain various life forms.",
    "img": null
  },
  "Disadvantages": {
    "point": "While photosynthesis is crucial, it has limitations. The process can be affected by factors such as limited light availability, water scarcity, and environmental stress. In some cases, excessive exposure to light can lead to photooxidative damage, disrupting the balance of the photosynthetic machinery.",
    "img": null
  },
  "Conclusion": {
    "point": "Photosynthesis is a fundamental process that drives the biosphere by converting light energy into chemical energy. It has a profound impact on the global environment, shaping ecosystems and supporting life. Understanding the mechanisms of photosynthesis can lead to advancements in agriculture, renewable energy, and environmental conservation.",
    "img": null
  }
}

and it has given the out put as:

{"Title": "फोटोसिन्थेसिस", 
    "परिचय": {
        "point": "फोटोसिन्थेसिस पौधों, श्वालज और कुछ जीवाणुओं में होने वाली एक महत्वपूर्ण जैविक प्रक्रिया है। इसमें प्रकाश ऊर्जा को खाद्य पदार्थ रूप में ग्लुकोज़ और अन्य कार्बनिक यौगिकों की रूप में रूपांतरित किया जाता है। यह प्रक्रिया पृथ्वी पर जीवन का सहारा देने वाले ऑक्सीजन का उत्पादन जिम्मेदार है।", 
        "img": "http://www.biology.arizona.edu/biochemistry/problem_sets/intro_photosynthesis/graphics/PSN-Reaction.jpg"}, 
    "इतिहास": {
        "point": "फोटोसिन्थेसिस की प्रक्रिया का अध्ययन पहली बार 18वीं सदी के अंत में जान इंगेनहौस द्वारा किया गया था। उन्होंने खंडक उज्ज्वलता के मौजूदगी में पौधों द्वारा ऑक्सीजन छोड़ा जाता है यह खोजी। 19वीं सदी की शुरुआत में, जूलियस वोन साक्स और थीयोडोर एंगलमैन जैसे शोधकर्ता ने फोटोसिन्थेसिस की समझ को और भी आगे बढ़ाया। हालांकि, फोटोसिन्थेसिस की पूर्ण तंत्रज्ञान हमें 20वीं सदी के मध्य तक मिला नहीं।", 
        "img": null
        }, 
    "काम का सिद्धांत": {
        "point": "फोटोसिन्थेसिस मुख्य रूप से पौधों के क्लोरोप्लास्ट में होती है। इस प्रक्रिया को दो चरणों में विभाजित किया जा सकता है: प्रकाश पर आधारित प्रतिक्रियाएं और प्रकाश-अनिर्देशित प्रतिक्रियाएं (कैल्विन चक्र)। प्रकाश पर आधारित प्रतिक्रियाओं में, क्लोरोफिल और अन्य रंगीन पदार्थों द्वारा प्रकाश ऊर्जा को अवशोषित किया जाता है, जिससे ATP और NADPH का उत्पादन होता है। ये ऊर्जा वाहक फिर कैल्विन चक्र में कार्बन डाइऑक्साइड को ग्लुकोज़ में परिवर्तित करने के लिए उपयोग किए जाते हैं।", 
        "img": "https://i1.rgstatic.net/publication/229062430_Principles_of_photosynthesis/links/6040afd3299bf1e078549aeb/largepreview.png"
        }, 
    "सिद्धांत का सबूत": {
        "point": "फोटोसिन्थेसिस कई मौलिक सिद्धांतों का पालन करता है:\n\n1. ऊर्जा संरक्षण का नियम फोटोसिन्थेसिस में लागू होता है। प्रक्रिया के पहले और बाद में प्रणाली में कुल ऊर्जा स्थिर रहती है।\n2. फोटोसिन्थेसिस की दर प्रकाश की तीव्रता, कार्बन डाइऑक्साइड घनत्व और तापमान जैसे कारकों पर प्रभावित होती है।\n3. फोटोसिन्थेसिस के लिए समग्र समीकरण है: 6 सीओ2 + 6 एच2ओ + प्रकाश ऊर्जा \u2192 C6H12O6 + 6 O2", 
        "img": "https://i.ytimg.com/vi/2a8FyieAYH4/maxresdefault.jpg"
        }, 
    "लाभ": {
        "point": "फोटोसिन्थेसिस पृथ्वी की पारिस्थितिकी को बनाए रखने में महत्वपूर्ण भूमिका निभाती है। यह ऑक्सीजन उत्पन्न करती है, जो सांस लेने और कई प्राणियों के जीवन के लिए आवश्यक है। इसके अलावा, फोटोसिन्थेसिस खाद्य श्रृंखला का आधार है, क्योंकि इससे ऊर्जा संग्रहीत जैविक अणुओं की उत्पादन होती है जो विभिन्न जीवन रूपों को पोषित करती हैं।", 
        "img": null
        },
    "असावधानियाँ": {
        "point": "फोटोसिन्थेसिस महत्वपूर्ण होती है, लेकिन इसकी सीमाएं होती हैं। प्रक्रिया को प्रभावित कर सकते हैं जैसे कि प्रकाश की उपलब्धता की सीमा, पानी की कमी और पर्यावरणीय तनाव। कुछ मामलों में, प्रकाश के अतिरिक्त संपर्क में आने से फोटोऑक्सीडेटिव क्षति हो सकती है, जो फोटोसिन्थेटिक यंत्र के संतुलन को विकर्षित करती है।",
          "img": null
          }, 
    "निष्कर्ष": {
        "point": "फोटोसिन्थेसिस एक मौलिक प्रक्रिया है जो प्रकाश ऊर्जा को रासायनिक ऊर्जा में परिवर्तित करके बायोस्फीयर को चलाती है। यह वैश्विक पर्यावरण पर गहरा प्रभाव डालती है, पारिस्थितिकी को आकार देती है और जीवन का समर्थन करती है। फोटोसिन्थेसिस के तंत्रों की मेकेनिज़्म को समझना कृषि, नवीनीकरणीय ऊर्जा और पर्यावरण संरक्षण में प्रगति कराने के लिए आवश्यक हो सकता है।", 
        "img": null
        }
    }
'''


import openai
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain import LLMChain
import json
# Set your OpenAI API key here
API_KEY = "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"
def lgchain(text, language):
    if language=="e":
        return ""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=API_KEY)
    template =""" translate the following json scipt into {a} language but use the words 'Title', 'point', 'img' as it is
    {b}
     note L also keep in mind that encoding must utf-8 that can be encodable in 'latin-1' and don't enclude '\\u2192' characters
     """
    prompt = PromptTemplate(template=template,input_variables=['a','b'])
    chain = LLMChain(llm=llm,prompt=prompt)
    input = {'a':language,'b':text}
    return chain.run(input)
# Load the JSON data
# with open('Pythagoras theorem.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)
# with open('Pythagorastheoremfrench.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(lgchain(json.dumps(data),"french"))
