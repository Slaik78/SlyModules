
from .. import loader, utils

@loader.tds
class NoHello(loader.Module):
    """Модуль для неприветов"""

    strings = {"name": "NoHello"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
            "listNoHello",
            ['привет', 'здарова', 'здаров', 'ку', 'пр'],
            lambda: "Добавляй текст, который не хочешь видеть.",
            validator=loader.validators.Series()
            ),
        )

    @loader.watcher(only_messages = True)
    async def watcher(self, message):
        if message.is_private:
            if message.text.lower() in self.config['listNoHello']:
                if message.from_id != self.tg_id:
                    await message.client.send_message(message.from_id, '<a href="https://nohello.net/ru">Прочти меня</a>', reply_to=message.id, link_preview=False)
