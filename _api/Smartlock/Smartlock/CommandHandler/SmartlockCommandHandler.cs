using Smartlock.Interfaces.CommandHandler;
using Smartlock.Interfaces.Repositorio.Escrita;
using Smartlock.Model;
using Smartlock.Repositorio;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Smartlock.Command
{
    public class SmartlockCommandHandler : ISmartlockCommandHandler
    {
        private readonly ISmartlockWriteRepository smartlockWriteRepository;

        public SmartlockCommandHandler(ISmartlockWriteRepository smartlockWriteRepository)
        {
            this.smartlockWriteRepository = smartlockWriteRepository;
        }

        public async Task InserirDigital(DigitalModel model)
        {
            if (string.IsNullOrWhiteSpace(model.Digital))
                throw new Exception();

            await smartlockWriteRepository.InserirDigital(model);
        }
    }
}
