import discord


class OptButtonView(discord.ui.View):
    def __init__(self, model_change_listener=None):
        super().__init__()
        self.model_change_listener = model_change_listener

    async def set_model_and_respond(self, model_name, interaction):
        if self.model_change_listener:
            self.model_change_listener(model_name)
        await interaction.response.send_message(f"Модель переключена на {model_name}", ephemeral=True)

    @discord.ui.button(label="GPT-3", style=discord.ButtonStyle.success)
    async def button_1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.set_model_and_respond('text-davinci-003', interaction)

    @discord.ui.button(label="GPT-3.5-turbo", style=discord.ButtonStyle.danger)
    async def button_2(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.set_model_and_respond('gpt-3.5-turbo', interaction)
