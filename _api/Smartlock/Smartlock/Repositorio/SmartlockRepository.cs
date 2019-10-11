using Npgsql;
using System;
using System.Collections.Generic;
using Dapper;
using Smartlock.Model;
using Smartlock.Command;
using System.Threading.Tasks;
using Smartlock.Interfaces.Repository;

namespace Smartlock.Repositorio
{
    public class SmartlockRepository : ISmartlockRepository
    {
        private ConnectionCommand command;
        public SmartlockRepository(ConnectionCommand command)
        {
            this.command = command;
        }

        public async Task<IEnumerable<Blob>> ObterImagens()
        {
            using(var conexao = command.GetConnection())
            {
                var query = @"SELECT id AS idimagem,
                                       imagem
                                FROM blobteste";

                return await conexao.QueryAsync<Blob>(query);
            }
        }
    }
}
