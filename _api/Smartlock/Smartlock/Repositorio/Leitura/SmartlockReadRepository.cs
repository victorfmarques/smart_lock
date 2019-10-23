using Npgsql;
using System;
using System.Collections.Generic;
using Dapper;
using Smartlock.Model;
using System.Threading.Tasks;
using Smartlock.Interfaces.Repository;
using InfraLibrary.BaseCommands;

namespace Smartlock.Repositorio
{
    public class SmartlockReadRepository : ISmartlockReadRepository
    {
        private ConnectionCommand command;
        public SmartlockReadRepository(ConnectionCommand command)
        {
            this.command = command;
        }

        public async Task<IEnumerable<DigitalModel>> ObterDigitais()
        {
            using (var conexao = command.SetarConnection())
            {
                var query = @"SELECT idusuario, digital
                                FROM usuariodigital";

                return await conexao.QueryAsync<DigitalModel>(query);
            }
        }
    }
}
