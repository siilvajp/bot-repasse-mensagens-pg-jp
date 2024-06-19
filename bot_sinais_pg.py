from telethon import TelegramClient, events
from senhas import api_hash, api_id
import asyncio

sessao = 'Repassar Mensagem'

def modificar_mensagem(mensagem):
    mensagem_modificada = mensagem.replace("https://bit.ly/SecrettlinkJP", "https://bit.ly/JPLink")
    mensagem_modificada = mensagem_modificada.replace("STARTBET", "Igame333")
    mensagem_modificada = mensagem_modificada.replace("Startbet", "Igame333")
    return mensagem_modificada

async def main():
    print('Monitoramento iniciado...')
    
    async with TelegramClient(sessao, api_id, api_hash) as client:
        
        @client.on(events.NewMessage(chats=[-1001981834705]))
        async def enviar_mensagem(event):
            print(f"Nova mensagem recebida: {event.message}")
            
            mensagem_original = event.raw_text if event.raw_text else ""
            mensagem_modificada = modificar_mensagem(mensagem_original)
            print(f"Mensagem original: {mensagem_original}")
            print(f"Mensagem modificada: {mensagem_modificada}")

            try:
                if event.media:
                    print("A mensagem contém mídia.")
                    await client.send_file(-1002217869608, event.media, caption=mensagem_modificada)
                    print("Mídia enviada com sucesso.")
                elif mensagem_modificada:
                    await client.send_message(-1002217869608, mensagem_modificada, parse_mode='HTML')
                    print("Mensagem enviada com sucesso.")
                else:
                    print("A mensagem modificada está vazia. Não enviando.")
            except Exception as e:
                print(f"Erro ao enviar mensagem ou mídia: {e}")
            
            if event.sticker:
                try:
                    # Enviar o sticker diretamente, sem baixar
                    sticker = event.message.media
                    await client.send_file(-1002217869608, sticker)
                    print("Sticker enviado com sucesso.")
                except Exception as e:
                    print(f"Erro ao enviar sticker: {e}")

        await client.run_until_disconnected()

asyncio.run(main())
