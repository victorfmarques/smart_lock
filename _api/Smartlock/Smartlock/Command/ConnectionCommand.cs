using Npgsql;
using System;

namespace Smartlock.Command
{
    public class ConnectionCommand : IDisposable
    {
        public ConnectionCommand()
        {
            this.conexao = new NpgsqlConnection();
        }
        public NpgsqlConnection conexao;

        public NpgsqlConnection GetConnection()
        {
            conexao.ConnectionString = Startup.ConnectionString;

            conexao.Open();

            return conexao;
        }

        public void Dispose()
        {
            if (conexao.State == System.Data.ConnectionState.Open)
                conexao.Close();
        }
    }
}
