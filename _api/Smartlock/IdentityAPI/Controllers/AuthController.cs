using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using IdentityAPI.Interfaces;
using IdentityAPI.Model;
using Microsoft.AspNetCore.Mvc;

namespace IdentityAPI.Controllers
{
    [Route("api/auth")]
    public class AuthController : Controller
    {
        [HttpPost("generatetoken")]
        public async Task<IActionResult> GenerateToken(
            [FromBody] AuthModel authModel,
            [FromServices] IAuthConnectionCommand connectionCommand,
            [FromServices] IJwtGenerationCommand jwtGenerationCommand
        )
        {
            authModel.Digitais = await connectionCommand.ObterDigitais(authModel.UserId);

            return Json(jwtGenerationCommand.GenerateToken(authModel));
        }
    }
}