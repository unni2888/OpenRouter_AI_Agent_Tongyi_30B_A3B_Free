from openai import OpenAI
from dotenv import load_dotenv

# First API call with reasoning
response = client.chat.completions.create(
  model="alibaba/tongyi-deepresearch-30b-a3b:free",
  messages=[
          {
            "role": "user",
            "content": "Hi"
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
)

# Extract the assistant message with reasoning_details
response = response.choices[0].message


# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": input},
  {
    "role": "assistant",
    "content": response.content,
    "reasoning_details": response.reasoning_details  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = client.chat.completions.create(
  model="alibaba/tongyi-deepresearch-30b-a3b:free",
  messages=messages,
  extra_body={"reasoning": {"enabled": True}}
)

#print("First response:", response.content)
#print("Second response:", response2.choices[0].message.con tent)
