# ED
'''
.ed:: Анимация, созданная для Империи Endless Destroy\n\n<b>Использование</b>: \n<code>.lv</code>
'''
import asyncio
from telethon import events
from asyncio import sleep
import random


phrases = [
'За империю!',
'ВАША ПОГИБЕЛЬ!',
'ЭТО КОНЕЦ!',
'ПОБЕДА ИМПЕРИИ ENDLESSDESTROY!',
'МЕСТЬ ПРЕЖДЕ ВСЕГО!',
'ВАШЕЙ ГРУППЕ КОНЕЦ!',
'БЕЗЖАЛОСТНОСТЬ - ЭТО СИЛА! ',
'ИМПЕРИЯ БЕСЦЕННА!'
]



def a(client):
	@client.on(events.NewMessage(pattern=r"\.ed", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return

		await event.edit('''
<b>.</b>''', parse_mode='html')
		await asyncio.sleep(0.5)

		await event.edit('''
▪️''')
		await asyncio.sleep(0.5)
		await event.edit('''
◼️''')
		await asyncio.sleep(0.5)
		await event.edit('''
🔳''')
		await asyncio.sleep(0.5)
		await event.edit('''
▫️▫️▫️
▫️🔳▫️
▫️▫️▫️''')
		await asyncio.sleep(0.5)

		await event.edit('''
◽️◽️◽️
◽️🔳◽️
◽️◽️◽️''')
		await asyncio.sleep(0.5)

		await event.edit('''
◻️◻️◻️
◻️🔳◻️
◻️◻️◻️''')
		await asyncio.sleep(0.5)
		await event.edit('''
⬜️⬜️⬜️
⬜️🔳⬜️
⬜️⬜️⬜️''')
		await asyncio.sleep(0.5)
		await event.edit('''
⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬜️
⬜️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️''')
		await asyncio.sleep(0.5)
		await event.edit('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬛️ 🅴 ⬛️⬜️
⬜️⬛️ 🅳 ⬛️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️''')
		await asyncio.sleep(1)
		await event.edit('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬛️ 🅔 ⬛️⬜️
⬜️⬛️ 🄳 ⬛️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️''')
		await asyncio.sleep(1)

		await event.edit('''
⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️
⬜️<b>ИМПЕРИЯ БЕСЦЕННА!</b>⬜️
⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️''', parse_mode='html')
		await asyncio.sleep(1)
		await event.edit('''
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️   <b>ВАШЕЙ ГРУППЕ КОНЕЦ</b>  ⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️''', parse_mode='html')
		await asyncio.sleep(1)
		await event.edit('''
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
🔲   <b>ВАШЕЙ ГРУППЕ КОНЕЦ</b>  🔲
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️''', parse_mode='html')
		await asyncio.sleep(1)
 
		await event.edit('''
💣💣💣💣💣💣💣💣💣💣
💣   <b>ВАШЕЙ ГРУППЕ КОНЕЦ</b>  💣
💣💣💣💣💣💣💣💣💣💣''', parse_mode='html')
		await asyncio.sleep(1)
		await event.edit('''
🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨
🧨   <b>ВАШЕЙ ГРУППЕ КОНЕЦ</b>  🧨
🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨''', parse_mode='html')
		await asyncio.sleep(1)
		await event.edit('''
💥💥💥💥💥💥💥💥💥💥
💥💥💥💥💥💥💥💥💥💥
💥💥💥💥💥💥💥💥💥💥''')
		await asyncio.sleep(1)
		await event.edit(f'''
🪦🪦🪦🪦🪦🪦🪦🪦🪦🪦
⚰️⚰️⚰️⚰️⚰️⚰️⚰️⚰️⚰️⚰️
🪬         МЕРТВАЯ ГРУППА          🪬
<b>>     {random.choice(phrases)}     <</b>''', parse_mode='html')
		await asyncio.sleep(1)
 


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass