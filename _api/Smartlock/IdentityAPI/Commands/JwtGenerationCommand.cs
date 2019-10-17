using IdentityAPI.Interfaces;
using IdentityAPI.Model;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.IdentityModel.Tokens;
using System;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

namespace IdentityAPI.Commands
{
    public class JwtGenerationCommand : IJwtGenerationCommand
    {
        private readonly IConfiguration configuration;
        private readonly IHostingEnvironment hostingEnvironment;

        public JwtGenerationCommand(IConfiguration configuration, IHostingEnvironment hostingEnvironment)
        {
            this.hostingEnvironment = hostingEnvironment;
            this.configuration = configuration;
        }
        public JwtSecurityToken GenerateToken(AuthModel model)
        {
            var issuer = configuration.GetSection("Jwt").GetValue<string>("Issuer");
            var audience = configuration["Audience"];
            var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(configuration["Jwt:Key"]));
            var credentials = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);
            var claims = ObterClaims(model);

            var tokenHandler = new JwtSecurityTokenHandler();

            return tokenHandler.CreateJwtSecurityToken(
                issuer, 
                audience,
                expires: DateTime.Now.AddDays(7),
                signingCredentials: credentials,
                subject: claims
            );
        }

        protected ClaimsIdentity ObterClaims(AuthModel model)
        {
            var claims = new ClaimsIdentity();
            claims.AddClaim(new Claim("Usuário", model.UserId.ToString()));
            var numeracao = 0;
            foreach(var digital in model.Digitais)
            {
                numeracao++;
                claims.AddClaim(new Claim("digital " + numeracao, digital));
            }

            return claims;
        }
    }
}
