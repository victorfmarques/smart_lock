using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Smartlock.Interfaces.Repositorio.Escrita;
using Smartlock.Interfaces.Repository;
using Smartlock.Model;
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace Smartlock.Controllers
{
    [Authorize]
    [Produces("application/json")]
    [Route("api/smartlock")]
    public class SmartlockController : Controller
    {
        private ISmartlockReadRepository smartlockReadRepository;
        private ISmartlockWriteRepository smartlockWriteRepository;

        public SmartlockController(ISmartlockReadRepository smartlockReadRepository, ISmartlockWriteRepository smartlockWriteRepository)
        {
            this.smartlockReadRepository = smartlockReadRepository;
            this.smartlockWriteRepository = smartlockWriteRepository;
        }

        [HttpGet("obterdigitais")]
        public async Task<IActionResult> ObterDigitais()
        {
            try
            {
                return Ok(await this.smartlockReadRepository.ObterDigitais());
            }
            catch
            {
                return BadRequest("deu ruim");
            }
        }

        [HttpPost("inserirdigital")]
        public async Task<IActionResult> InserirDigital([FromBody] DigitalModel model)
        {
            try
            {
                await smartlockWriteRepository.InserirDigital(model);
                return Ok();
            }
            catch
            {
                return BadRequest("Não inseriu não");
            }
        }
    }
}