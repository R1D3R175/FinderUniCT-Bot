# Finder-UniCT Bot
A Telegram bot for [UNICT (University of Catania)](https://www.unict.it/en) students enabling them to connect semi-anonymously.  

## Features
- **Login**: Authenticate with your UniCT email.
- **Random Chat**: Engage in conversations with strangers.
- **Interest Matching**: Specify your interests and connect with students of similar tastes.
- **Global Chat**: Join a community chat with all UniCT students.

> **Note**: The bot commands and their responses are in Italian. Use `/start` to initiate and `/help` for a command list.

## Getting Started

### Obtain a Telegram Bot Token
1. Open Telegram and search for @BotFather.
2. Start a conversation with `/start`.
3. Create a new bot using `/newbot`.
4. Name your bot and assign a tag (it should end with `bot`).
5. Copy the provided token.

# Usage
The bot operates through a set of commands and reacts to specific triggers. Below is an overview of the bot's main commands and their descriptions:

/start: Sends a welcome message. (Translation: messaggio di benvenuto)
/help: Provides guidance on available commands. (Translation: ricevi aiuto sui comandi)
/report: Allows users to report an issue or problem. (Translation: segnala un problema)
/chatid: Returns the chat ID of the current conversation. This can be useful for debugging and administration purposes.
The bot is also programmed to handle messages and commands in private chats, ensuring the safety and privacy of user interactions.

### Running with Docker
#### Using Docker Compose

```yaml
version: '2'
services:
  finderdmibot:
    image: ghcr.io/unict-dmi/finderunictbot
    container_name: finderunictbot
    volumes:
      - <path-to-your-settings.yaml>:/app/config/settings.yaml
    restart: unless-stopped

```
**Local Build**:

\```bash
git clone git@github.com:UNICT-DMI/FinderUniCT-Bot.git
cd FinderUniCT-Bot
docker build --tag finderunictbot .
\```

#### Using Docker CLI

1. Clone the repository.
2. Make a copy of `config/settings.yaml.dist` and rename it to `config/settings.yaml`.
3. Add your Telegram bot's token in the `token` field.
4. Build the image: `docker build -t finderunictbot .`
5. Run:

   - On Windows:
     \```bash
     docker run -v "C:\path\to\your\settings.yaml:/finderunictbot/config/settings.yaml" finderunictbot
     \```
     
   - On Linux:
     \```bash
     docker run -v "/path/to/your/settings.yaml:/finderunictbot/config/settings.yaml" finderunictbot
     \```

### Running Natively

1. Clone this repository.
2. Copy `config/settings.yaml.dist` to `config/settings.yaml`.
3. Update the `token` field with your Telegram bot's token.
4. Execute: `python main.py`.

## Credits
