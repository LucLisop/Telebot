# Love
'''
.love:: Анимация. \n\n<b>Использование</b>: <code>.love</code> ваштекст
'''
from telethon import events
import asyncio


def a(client):
	@client.on(events.NewMessage(pattern=r"\.love", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		await event.edit('''
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)
		await event.edit('''
❤️❤️❤️❤️❤️❤️❤️❤️
❤️💛❤️💛❤️💛❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️💛❤️💛❤️💛❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️💛❤️💛❤️💛❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)
		await event.edit('''
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚''')
		await asyncio.sleep(0.5)
		await event.edit('''
💚💚💚💚💚💚💚💚
💚💚💚💚🖤💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚''')
		await asyncio.sleep(0.5)
		await event.edit('''
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚🖤💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚''')
		await asyncio.sleep(0.5)

		await event.edit('''
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚🖤💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚''')
		await asyncio.sleep(0.5)
		await event.edit('''
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚🖤💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚''')
		await asyncio.sleep(0.5)
		await event.edit('''
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚🖤💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚''')
		await asyncio.sleep(0.5)

		await event.edit('''
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚🖤💚💚💚
💚💚💚💚💚💚💚💚''')
		await asyncio.sleep(0.5)

		await event.edit('''
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)

		await event.edit('''
💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙''')
		await asyncio.sleep(0.5)
		await event.edit('''
💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜''')
		await asyncio.sleep(0.5)
		await event.edit('''
🧡🧡🧡🧡🧡🧡🧡🧡
🧡🧡🧡🧡🧡🧡🧡🧡
🧡🧡🧡🧡🧡🧡🧡🧡
🧡🧡🧡🧡🧡🧡🧡🧡
🧡🧡🧡🧡🧡🧡🧡🧡
🧡🧡🧡🧡🧡🧡🧡🧡
🧡🧡🧡🧡🧡🧡🧡🧡
🧡🧡🧡🧡🧡🧡🧡🧡''')
		await asyncio.sleep(0.5)
		await event.edit('''
🤎🤎🤎🤎🤎🤎🤎🤎
🤎🤎🤎🤎🤎🤎🤎🤎
🤎🤎🤎🤎🤎🤎🤎🤎
🤎🤎🤎🤎🤎🤎🤎🤎
🤎🤎🤎🤎🤎🤎🤎🤎
🤎🤎🤎🤎🤎🤎🤎🤎
🤎🤎🤎🤎🤎🤎🤎🤎
🤎🤎🤎🤎🤎🤎🤎🤎''')
		await asyncio.sleep(0.5)

		await event.edit('''
💛💛💛💛💛💛💛💛
💛💛💛💛💛💛💛💛
💛💛💛💛💛💛💛💛
💛💛💛💛💛💛💛💛
💛💛💛💛💛💛💛💛
💛💛💛💛💛💛💛💛
💛💛💛💛💛💛💛💛
💛💛💛💛💛💛💛💛''')
		await asyncio.sleep(0.5)

		await event.edit('''
🤍🤍🤍🤍🤍🤍🤍🤍
🤍🖤🖤🖤🖤🖤🖤🤍
🤍🖤🤍🤍🤍🤍🖤🤍
🤍🖤🤍🖤🖤🤍🖤🤍
🤍🖤🤍🖤🖤🤍🖤🤍
🤍🖤🤍🤍🤍🤍🖤🤍
🤍🖤🖤🖤🖤🖤🖤🤍
🤍🤍🤍🤍🤍🤍🤍🤍''')
		await asyncio.sleep(0.5)
		await event.edit('''
🖤🖤🖤🖤🖤🖤🖤🖤
🖤🤍🤍🤍🤍🤍🤍🖤
🖤🤍🖤🖤🖤🖤🤍🖤
🖤🤍🖤🤍🤍🖤🤍🖤
🖤🤍🖤🤍🤍🖤🤍🖤
🖤🤍🖤🖤🖤🖤🤍🖤
🖤🤍🤍🤍🤍🤍🤍🖤
🖤🖤🖤🖤🖤🖤🖤🖤''')
		await asyncio.sleep(0.5)
		await event.edit('''
🤍🤍🤍🤍🤍🤍🤍🤍
🤍🖤🖤🖤🖤🖤🖤🤍
🤍🖤🤍🤍🤍🤍🖤🤍
🤍🖤🤍🖤🖤🤍🖤🤍
🤍🖤🤍🖤🖤🤍🖤🤍
🤍🖤🤍🤍🤍🤍🖤🤍
🤍🖤🖤🖤🖤🖤🖤🤍
🤍🤍🤍🤍🤍🤍🤍🤍''')
		await asyncio.sleep(0.5)
		await event.edit('''
🖤🖤🖤🖤🖤🖤🖤🖤
🖤🤍🤍🤍🤍🤍🤍🖤
🖤🤍🖤🖤🖤🖤🤍🖤
🖤🤍🖤🤍🤍🖤🤍🖤
🖤🤍🖤🤍🤍🖤🤍🖤
🖤🤍🖤🖤🖤🖤🤍🖤
🖤🤍🤍🤍🤍🤍🤍🖤
🖤🖤🖤🖤🖤🖤🖤🖤''')
		await asyncio.sleep(0.5)
		await event.edit('''
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)
		await event.edit('''
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)

		await event.edit('''
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)
		await event.edit('''
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)
		await event.edit('''
❤️❤️❤️❤️
❤️❤️❤️❤️
❤️❤️❤️❤️
❤️❤️❤️❤️''')
		await asyncio.sleep(0.5)
 
		await event.edit('''
❤️❤️❤️
❤️❤️❤️
❤️❤️❤️''')
		await asyncio.sleep(0.5)
		await event.edit('''
❤️❤️
❤️❤️''')
		await asyncio.sleep(0.5)
		await event.edit('''
❤️''')
		await asyncio.sleep(0.5)
 


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass