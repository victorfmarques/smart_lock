using InfraLibrary.BaseCommands;
using Smartlock.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Dapper;

namespace Smartlock.Repositorio
{
    public class SmartlockWriteRepository
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
                var query = "INSERT INTO usuariodigital (idusuario, digital) VALUES (@idUsuario, @digital)";
                await conexao.ExecuteAsync(query, new { @idUsuario = model.IdUsuario, @digital = model.Digital} );
            }
        }
    }
}
