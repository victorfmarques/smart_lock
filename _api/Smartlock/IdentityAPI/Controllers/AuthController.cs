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
            //authModel.Digitais = await connectionCommand.ObterDigitais(authModel.UserId);

            return Ok(jwtGenerationCommand.GenerateToken(authModel));
        }

        [HttpPost("inserirdigital")]
        public async Task<IActionResult> InserirDigital(
            [FromBody] DigitalModel model,
            [FromServices] IAuthConnectionCommand command
        )
        {
            await command.InserirDigital(model);
            return Ok();
        }
    }
}