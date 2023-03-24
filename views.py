import discord


class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Выбор 1", style=discord.ButtonStyle.success)
    async def button_1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Вы выбрали 1", ephemeral=True)

    @discord.ui.button(label="Выбор 2", style=discord.ButtonStyle.danger)
    async def button_2(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Вы выбрали 2", ephemeral=True)

    @discord.ui.button(label="Выбор 3", style=discord.ButtonStyle.primary)
    async def button_3(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Вы выбрали 3", ephemeral=True)
