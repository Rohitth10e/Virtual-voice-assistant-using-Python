import openai
import os

# Set your OpenAI API key
api_key = os.environ.get('your api key')
openai.api_key = 'your api key'

# Create a completion request

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an eassy on sports\nwrite an eassy on sports\nSports have been an integral part of human society since ancient times. From the gladiator fights in ancient Rome to the modern-day Olympics, sports have always captured the attention and interest of people. Today, sports have evolved into a global industry, generating billions of dollars in revenue and creating a worldwide fan base.\n\nThe importance of sports goes beyond just physical fitness and entertainment. They offer a range of benefits that contribute to the overall development of individuals, communities, and even nations. One of the most significant advantages of sports is its ability to promote a healthy lifestyle. Engaging in physical activity through sports helps improve cardiovascular health, strengthen muscles and bones, and reduce the risk of chronic diseases. It also promotes mental well-being as it reduces stress, anxiety, and depression.\n\nFurthermore, sports have the power to bring people together, regardless of their cultural, social, or economic differences. It creates a sense of unity and camaraderie among players, supporters, and the entire community. People from all backgrounds come together to support their favorite team or athlete, creating a sense of belonging and connection. This bonding experience strengthens social ties, promotes cultural exchange, and builds a more cohesive society.\n\nSports also teach valuable life lessons, such as teamwork, discipline, and perseverance. In a team sport, players",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
generated_text = response['choices'][0]['text']
print(generated_text)


'''{
  "id": "cmpl-8bSiUwBDHhYMiEhkwAUhZi2gixb6e",
  "object": "text_completion",
  "created": 1703939214,
  "model": "davinci-002",
  "choices": [
    {
      "text": "8/8/2012 Thanks for the mail in English. Thread: New Job 1 reply.I would like to personally resign from my position effective 6/30/2012 onPlease advice me how to format the letter and please also include How to write an email to a boss? How to Write a Resignation Email that Leaves a Positive Impression? Raja Screen-Shot-2015-05-21-at-2.41.55-PM.Employee \u201cTakeover\u201d email announcement? 0. Sample email letter of resignation to boss. Thank you email after a phone interview what to include dear medtech Chronicles resignation of resignation via email for charity we get more than ever. Yourself up to a great text examples of resign letter to bossFor resign letter to write a good impression of resignation letter for informing your company, name and heres an effective. Exit email to keep all the The purpose of the resignation letter is to be informed about by the company so that you research paper on how to sample cover letter for a teachers resume write a Financial Analyst EmailTo Boss For resignation in hindi sample email to boss for resignation in hindi hindi english wikipedia Cashier resignation letter email examples how to write a letter of resignation howtopout. Fishing Resignation Letter.How",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 265,
    "completion_tokens": 256,
    "total_tokens": 521
  }
}'''