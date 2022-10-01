# Report
'''
.report:: Жалоба на чат\n\n<b>Использование</b>: \n<code>.report</code> <Комментарий к жалобе>(по желанию)
'''
import asyncio
from telethon import events
from asyncio import sleep
import random
from telethon import events, types, functions, errors, TelegramClient


reasons = [
types.InputReportReasonChildAbuse(),
types.InputReportReasonCopyright(),
types.InputReportReasonFake(),
types.InputReportReasonPornography(),
types.InputReportReasonSpam(),
types.InputReportReasonViolence(),
types.InputReportReasonOther()]



def a(client):
	@client.on(events.NewMessage(pattern=r"\.report", outgoing=True))
	async def _(event):
		print(event.stringify())
		args = str(event.message.text).split(' ')
		

		if len(args) < 2:
			comment = 'Delete chat!'
		else:
			comment = ' '.join(args[1:])
			print(comment)

		for reason in reasons:
			
			result = await client(
				functions.account.ReportPeerRequest(
					peer=event.peer_id,
					reason=reason,
					message=comment
				)
			)
			try:
				await event.edit(f'Жалоба {str(reason)} отправлена!')
			except Exception as e:
				print(e)

		await event.edit(f'<b>Жалобы успешно отправлены!</b>',parse_mode='html')


		
		
 


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass
