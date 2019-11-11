using InfraLibrary.BaseCommands;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Smartlock.Command;
using Smartlock.Interfaces.CommandHandler;
using Smartlock.Interfaces.Repositorio.Escrita;
using Smartlock.Interfaces.Repository;
using Smartlock.Repositorio;

namespace Smartlock
{
    public class Startup
    {
        public static string ConnectionString;

        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
            ConnectionString = Configuration["ConnectionStrings:Smartlock"];
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc();
            services.AddScoped<ISmartlockReadRepository, SmartlockReadRepository>();
            services.AddScoped<ISmartlockCommandHandler, SmartlockCommandHandler>();
            services.AddScoped<ISmartlockWriteRepository, SmartlockWriteRepository>();
            services.AddScoped(typeof(ConnectionCommand));

            //services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme).AddJwtBearer(options =>
            //{
            //    options.TokenValidationParameters = new TokenValidationParameters()
            //    {
            //        ValidateActor = false,
            //        ValidateAudience = false,
            //        ValidateLifetime = false,
            //        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Configuration["Jwt:Key"])),
            //        ClockSkew = TimeSpan.Zero
            //    };
            //});
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseMvc();
        }
    }
}
