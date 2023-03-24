import discord
import os


class OptButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="GPT-3", style=discord.ButtonStyle.success)
    async def button_1(self, button: discord.ui.Button, interaction: discord.Interaction):
        global current_model
        current_model = 'text-davinci-003'
        with open("model.db", "w") as file:
            file.write(current_model)
        await interaction.response.send_message("Модель переключена на text-davinci-003", ephemeral=True)

    @discord.ui.button(label="GPT-3.5-turbo", style=discord.ButtonStyle.danger)
    async def button_2(self, button: discord.ui.Button, interaction: discord.Interaction):
        global current_model
        current_model = 'gpt-3.5-turbo'
        with open("model.db", "w") as file:
            file.write(current_model)
        await interaction.response.send_message("Модель переключена на gpt-3.5-turbo", ephemeral=True)

    """
    @discord.ui.button(label="Выбор 3", style=discord.ButtonStyle.primary)
    async def button_3(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Вы выбрали 3", ephemeral=True)
    """
