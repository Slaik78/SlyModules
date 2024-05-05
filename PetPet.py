#------------------------------------------------------------------
#      ___           ___       ___                       ___     
#     /\  \         /\__\     /\  \          ___        /\__\    
#    /::\  \       /:/  /    /::\  \        /\  \      /:/  /    
#   /:/\ \  \     /:/  /    /:/\:\  \       \:\  \    /:/__/     
#  _\:\~\ \  \   /:/  /    /::\~\:\  \      /::\__\  /::\__\____ 
# /\ \:\ \ \__\ /:/__/    /:/\:\ \:\__\  __/:/\/__/ /:/\:::::\__\
# \:\ \:\ \/__/ \:\  \    \/__\:\/:/  / /\/:/  /    \/_|:|~~|~   
#  \:\ \:\__\    \:\  \        \::/  /  \::/__/        |:|  |    
#   \:\/:/  /     \:\  \       /:/  /    \:\__\        |:|  |    
#    \::/  /       \:\__\     /:/  /      \/__/        |:|  |    
#     \/__/         \/__/     \/__/                     \|__|   
#------------------------------------------------------------------ 
# meta developer: @hicota
# requires: pet-pet-gif

import os
from hikkatl.types import Message
from .. import loader, utils
from io import BytesIO
from petpetgif import petpet


@loader.tds
class PetPetMod(loader.Module):
    """Развлекательный модуль"""
    
    strings = {"name": "PetPet"}

    @loader.command()
    async def pet(self, message: Message):
        """гладит фото"""
        response = await message.get_reply_message()
    
        try:
            media = await self._client.download_media(response.photo, "pet")
            petgif = BytesIO()
            petpet.make(media, petgif)
            petgif.name = "pet.gif"
            petgif.seek(0)
        except AttributeError :
            await utils.answer(message, '<emoji document_id=5465665476971471368>❌</emoji><b>Это не фото</b><emoji document_id=5465665476971471368>❌</emoji>\nОтветьте на фото чтобы команда .pet заработала')
            return

        await self._client.send_file(message.to_id, file=petgif, force_document=False)
        await message.delete()
        os.remove(media)