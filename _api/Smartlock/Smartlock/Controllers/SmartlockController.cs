using Microsoft.AspNetCore.Mvc;
using Smartlock.Interfaces.Repository;
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace Smartlock.Controllers
{
    [Produces("application/json")]
    [Route("api/smartlock")]
    public class SmartlockController : Controller
    {
        private ISmartlockRepository smartlockRepository;

        public SmartlockController(ISmartlockRepository smartlockRepository)
        {
            this.smartlockRepository = smartlockRepository;
        }

        [HttpGet("obterimagens")]
        public async Task<IActionResult> ObterImagens()
        {
            var imagens = await smartlockRepository.ObterImagens();
            var stream = imagens.Select(s => s.Imagem).FirstOrDefault();
            var str = System.Text.Encoding.Default.GetString(stream);
            var imagemBinaria = hex2binary(str);
            return Ok(imagemBinaria);
        }

        private string hex2binary(string hexvalue)
        {
            string binaryval = "";
            binaryval = Convert.ToString(Convert.ToInt32(hexvalue, 16), 2);
            return binaryval;
        }
    }
}