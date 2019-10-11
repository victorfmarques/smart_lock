using System.Collections.Generic;
using System.Threading.Tasks;
using InfraLibrary.BaseCommands;
using Microsoft.Extensions.Configuration;
using Dapper;
using IdentityAPI.Interfaces;

namespace IdentityAPI.Commands
{
    public class AuthConnectionCommand : ConnectionCommand, IAuthConnectionCommand
    {
        public AuthConnectionCommand(IConfiguration configuration): base(configuration)
        {

        }

        public async Task<IEnumerable<string>> ObterDigitais(int idUsuario)
        {
            using (var conexao = SetarConnection(ConnectionString))
            {
                var query = @"SELECT digital
                              FROM usuariodigital
                              WHERE idusuario = @idUsuario";

                return await conexao.QueryAsync<string>(query, new { idUsuario });
            }
        }
    }
}