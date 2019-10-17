using Dapper;
using IdentityAPI.Interfaces;
using IdentityAPI.Model;
using InfraLibrary.BaseCommands;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Threading.Tasks;

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

        public async Task InserirDigital(DigitalModel model)
        {
            using(var conexao = SetarConnection(ConnectionString))
            {
                var query = @"INSERT INTO usuariodigital (idusuario,digital)
                               VALUES(@idUsuario, @digital)";

                await conexao.ExecuteAsync(query, new { idUsuario = model.UserId, digital = model.Digital });
            }
        } 
    }
}