using System.Collections.Generic;
using System.Threading.Tasks;

namespace IdentityAPI.Interfaces
{
    public interface IAuthConnectionCommand
    {
        Task<IEnumerable<string>> ObterDigitais(int idUsuario);
    }
}
