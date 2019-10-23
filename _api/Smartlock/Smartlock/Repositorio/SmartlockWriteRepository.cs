using InfraLibrary.BaseCommands;
using Smartlock.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Dapper;
using Smartlock.Interfaces.Repositorio.Escrita;

namespace Smartlock.Repositorio
{
    public class SmartlockWriteRepository : ISmartlockWriteRepository
    {
        private readonly ConnectionCommand connectionCommand;
        public SmartlockWriteRepository(ConnectionCommand connectionCommand)
        {
            this.connectionCommand = connectionCommand;
        }
        public async Task InserirDigital(DigitalModel model)
        {
            using(var conexao = connectionCommand.SetarConnection())
            {
                var query = "INSERT INTO usuariodigital (idusuario, digital) VALUES (@IdUsuario, @Digital)";
                await conexao.ExecuteAsync(query, model );
            }
        }
    }
}
