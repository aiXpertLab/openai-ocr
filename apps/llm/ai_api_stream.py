import openai, streamlit as st
import time, json

from apps.llm.prompt_engineer import system_prompt

import dotenv
CFG = dotenv.dotenv_values(".env")
age = 300 # seconds

if 'ai_model' not in st.session_state:
    st.session_state.ai_model = "OpenAI"  # Initial value

ai_model = st.session_state.ai_model

if ai_model == "DeepSeek":
    client = openai.OpenAI(api_key = CFG['DS_API_KEY'], base_url="https://api.deepseek.com")
    model = "deepseek-chat"
    stream=False
else:
    client = openai.OpenAI(api_key = CFG['OPENAI_API_KEY'])
    model = "gpt-4o"
    stream=True


def extract_from_b64(base64_image, page_number):
    st.warning(ai_model)
    
    response = client.chat.completions.create(
        model=model,
        response_format={ "type": "json_object" },
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "extract the data in this bank statement and output into JSON "},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}", "detail": "high"}}
                ]
            }
        ],
        temperature=0.0,
        stream=stream
    )

    if stream:
        result=""
        start_time = time.time()

        for chunk in response:
            elapsed_time = time.time() - start_time
            
            if elapsed_time > age: 
                st.write(f"time used: {elapsed_time:.0f} seconds")
                result = json.dumps({"NOTICE": f"Page {page_number} not extracted due to time limit."})
                break
            
            if chunk.choices[0].delta.content is not None:
                result += chunk.choices[0].delta.content
        
        st.info(f"used time: {elapsed_time:.0f} seconds")
        return result
    else:
        st.write(response)
        return response.choices[0].message.content
