import asyncio
import g4f
import random
from func.translation import translate

async def translate_runs_asyncio(runs):
    tasks = []
    providers = [
        g4f.Provider.GptGo, 
        g4f.Provider.ChatBase,
    ]
    for i,(runs,text) in enumerate(runs):
        prov = random.choice(providers)
        delay = i
        tasks.append(asyncio.create_task(translate(runs,text, prov, delay)))
    return await asyncio.gather(*tasks)

def translate_runs(runs_batch:list):
    result = asyncio.run(translate_runs_asyncio(runs_batch))
    return result

def get_batch_translation(runs_batch:list):
    '''
    tasks = [[runs,text],[runs,text],....]
    '''
    runs = translate_runs(runs_batch)
    return runs