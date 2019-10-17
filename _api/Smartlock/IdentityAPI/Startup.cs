using IdentityAPI.Commands;
using IdentityAPI.Interfaces;
using InfraLibrary.BaseCommands;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace IdentityAPI
{
    public class Startup
    {
        public string ConnectionString { get; set; }
        public IConfiguration Configuration { get; }


        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
            ConnectionString = configuration.GetConnectionString("Auth");
        }


        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc().SetCompatibilityVersion(CompatibilityVersion.Version_2_1);
            services.AddScoped(typeof(ConnectionCommand));
            services.AddScoped<IAuthConnectionCommand, AuthConnectionCommand>();
            services.AddScoped<IJwtGenerationCommand, JwtGenerationCommand>();
            var value = Configuration["Jwt"];
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            var value = Configuration["Jwt"];

            app.UseMvc();
        }
    }
}
