using System;
using Telegram.Bot.Types;
using Telegram.Bot;


namespace BLL
{
    public abstract class Command
    {
        private string Name { get; }

        public abstract void Execute(Message message, TelegramBotClient client);

        public bool Contains(string command)
        {
            return command.Contains(this.Name);
        }
    }
}
