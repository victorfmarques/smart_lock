using IdentityAPI.Model;
using System.IdentityModel.Tokens.Jwt;

namespace IdentityAPI.Interfaces
{
    public interface IJwtGenerationCommand
    {
        JwtSecurityToken GenerateToken(AuthModel model);
    }
}
