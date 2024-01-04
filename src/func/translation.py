import g4f
import random
import ast


def translate(text, prov = g4f.Provider.GeekGpt):
    providers = [
        g4f.Provider.Bing, 
        g4f.Provider.GeekGpt, 
        g4f.Provider.GptChatly, 
        g4f.Provider.Liaobots
        ]
    if text:
        # context = 'Return ONLY Translation on English as python list (all elements are related in meaning). Use variable "translation = " and double quotes for elements, return exactly the same number of elements as you received (if initial list has 3 elements - you must return list with 3 elements, thats important): '
        context = f'Return ONLY python list with {len(text)} elements with ONLY translation on English (all elements are related in meaning), use variable "translation = " and double quotes for elements: '
        pull_text = ''
        pull_text = get_GPT_res(context, text, prov)
        if not pull_text:
            return translate(text, prov= random.choice(providers))
        pull_list = check_str(pull_text, len(text))
        if pull_list:
            return pull_list
        else:
            return translate(text, prov= random.choice(providers))
        

def make_list(pre_list:str):
    sep = '"'
    corr_list = []
    pre_corr_list = pre_list.split(sep)
    for i, el in enumerate(pre_corr_list):
        if i % 2 == 0:
            corr_list.append(el)

    return corr_list


def check_str(text, limit):
    if "```python" in text:
        text = text.split("```python")[-1]
        if "```" in text:
            text = text.split("```")[0]

    if "translation = " in text:
        sep = "translation = "
    elif "Translation = " in text:
        sep = "Translation = "
    else:
        return None
    
    text_pre_corr = text.split(sep)[-1]
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


def get_GPT_res(context, text, prov):
    try:
        request = context+str(text)
        response = g4f.ChatCompletion.create(
                    model="gpt-4-0613",
                    provider=prov, 
                    messages=[{"role": "user", "content": request}],)
        pull_text = ''.join([message for message in response])
        return pull_text
    except Exception:
        return None
   