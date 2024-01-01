import g4f
import random


def translate(text, prov = g4f.Provider.GeekGpt):
    dict_translations = {}
    providers = [
        g4f.Provider.Bing, 
        g4f.Provider.GeekGpt, 
        g4f.Provider.GptChatly, 
        g4f.Provider.Liaobots
        ]
    if text:
        context = "Return ONLY Translation on English as python list (that's important): "
        pull_text = ''
        pull_text = get_GPT_res(context, text, prov)
        if not pull_text:
            return translate(text, prov= random.choice(providers))
        pull_text_corr = check_str(pull_text)
        if pull_text_corr:
            return pull_text_corr
        else:
            return translate(text, prov= random.choice(providers))
    

def check_str(text):
    if "[" not in text:
        return None
    if "]" not in text:
        return None
    indexes_bracket_open = [i for i in range(len(text)) if text[i] == '[']
    indexes_bracket_close = [i for i in range(len(text)) if text[i] == ']']
    text_pre_corr = text[indexes_bracket_open[0]+1: indexes_bracket_close[-1]]
    if "'" in text_pre_corr and '"' in text_pre_corr:
        indexes_first = [i for i in range(len(text_pre_corr)) if text_pre_corr[i] == '"']
        indexes_second = [i for i in range(len(text_pre_corr)) if text_pre_corr[i] == "'"]
        if indexes_first[0] < indexes_second[0]:
            sep = '"'
            indexes = indexes_first
        else:
            sep = "'"
            indexes = indexes_second
    elif "'" in text_pre_corr:
        sep = "'"
        indexes = [i for i in range(len(text_pre_corr)) if text_pre_corr[i] == "'"]
    elif '"' in text_pre_corr:
        sep = '"'
        indexes = [i for i in range(len(text_pre_corr)) if text_pre_corr[i] == '"']
    else:
        return None
    
    corr_str = text_pre_corr[indexes[0]+1: indexes[-1]]
    return corr_str

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
   