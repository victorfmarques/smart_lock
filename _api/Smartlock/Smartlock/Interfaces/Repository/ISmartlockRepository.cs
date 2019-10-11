using Smartlock.Model;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Smartlock.Interfaces.Repository
{
    public interface ISmartlockRepository
    {
        Task<IEnumerable<Blob>> ObterImagens();
    }
}
