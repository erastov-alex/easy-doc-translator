import asyncio
import g4f
import random
import ast
from globals import counter


async def translate(runs, text, prov, delay):
    # providers = [
    #     g4f.Provider.Bing, 
    #     g4f.Provider.GeekGpt, 
    #     ]
    
    providers = [
        g4f.Provider.GptGo, 
        g4f.Provider.ChatBase,
    ]
    # providers = [
    #     g4f.Provider.ChatBase,
    #     g4f.Provider.Bing,
    #     g4f.Provider.You,
    #     g4f.Provider.Yqcloud,
    # ]
    #     g4f.Provider.Bing
    # ]

    if text:
        await asyncio.sleep(delay)
        while True:
            # context = 'Return ONLY Translation on English as python list (all elements are related in meaning). Use variable "translation = " and double quotes for elements, return exactly the same number of elements as you received (if initial list has 3 elements - you must return list with 3 elements, thats important): '
            context = f'Return python code with python list with {len(text)} elements with ONLY translation on English (all elements are related in meaning), use variable "translation = " and double quotes for translated elements: '
            pull_text = await get_GPT_response(context, text, prov)
            prov= random.choice(providers)
            if pull_text:
                pull_list = transform_str(pull_text, len(text))
                if pull_list:
                    return [runs, pull_list]
        

def make_list(pre_list:str):
    sep = '"'
    corr_list = []
    pre_corr_list = pre_list.split(sep)
    for i, el in enumerate(pre_corr_list):
        if i % 2 == 0:
            corr_list.append(el)
    return corr_list


def transform_str(text, limit):
    if "```python" in text:
        text = text.split("```python")[-1]
        if "```" in text:
            text = text.split("```")[0]

    if "translation = " in text:
        sep = "translation = "
        text_pre_corr = text.split(sep)[-1]
    elif "Translation = " in text:
        sep = "Translation = "
        text_pre_corr = text.split(sep)[-1]
    else:
        text_pre_corr = text
    
    if "[" in text_pre_corr and "]" in text_pre_corr:
        text_pre_corr = "[".join(text_pre_corr.split("[")[1:])
        text_pre_corr = "]".join(text_pre_corr.split("]")[:-1])
    else:
        return None
    if limit == 1:
        return [text_pre_corr[1:-1]]
    else:
        text_pre_corr = f"[{text_pre_corr}]"
        try:
            okey_list = ast.literal_eval(text_pre_corr)
        except Exception:
            okey_list = make_list(text_pre_corr)
        if len(okey_list) == limit:
            return okey_list
        else:
            return None


async def get_GPT_response(context, text, prov):
    await asyncio.sleep(2)
    try:
        request = context+str(text)
        response = await g4f.ChatCompletion.create_async(
                    model=g4f.models.gpt_35_turbo,
                    provider=prov, 
                    messages=[{"role": "user", "content": request}],)
        pull_text = ''.join([message for message in response])
        return pull_text
    except Exception as e:
        counter.add(1)
        return None
   