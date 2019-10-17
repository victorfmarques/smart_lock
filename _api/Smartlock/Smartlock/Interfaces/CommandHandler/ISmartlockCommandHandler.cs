using Smartlock.Model;
using System.Threading.Tasks;

namespace Smartlock.Interfaces.CommandHandler
{
    public interface ISmartlockCommandHandler
    {
        Task InserirDigital(DigitalModel model);
    }
}
