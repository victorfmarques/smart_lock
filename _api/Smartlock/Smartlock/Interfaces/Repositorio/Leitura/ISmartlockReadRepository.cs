using Smartlock.Model;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Smartlock.Interfaces.Repository
{
    public interface ISmartlockReadRepository
    {
        Task<IEnumerable<DigitalModel>> ObterDigitais();
    }
}
