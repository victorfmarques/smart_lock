using Smartlock.Model;
using System.Threading.Tasks;

namespace Smartlock.Interfaces.Repositorio.Escrita
{
    public interface ISmartlockWriteRepository
    {
        Task InserirDigital(DigitalModel model);
    }
}
