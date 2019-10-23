using Microsoft.Extensions.Configuration;
using Npgsql;
using System;
using System.Data;

namespace InfraLibrary.BaseCommands
{
    public class ConnectionCommand : IDisposable, IDbConnection
    {
        protected IDbConnection conexao;
        protected readonly IConfiguration configuration;

        public ConnectionCommand(IConfiguration configuration)
        {
            this.configuration = configuration;
        }

        public string ConnectionString { get => "User Id=smartlock;Password=ubuntulixo;Host=smartlock.crekutelavgm.us-east-2.rds.amazonaws.com;Port=5432;Database=smartlock"; set => throw new NotImplementedException(); }

        public int ConnectionTimeout => 7200;

        public string Database => "Smartlock";

        public ConnectionState State => throw new NotImplementedException();

        public IDbConnection SetarConnection(string conexao = null)
        {
            this.conexao = new NpgsqlConnection
            {
                ConnectionString = string.IsNullOrWhiteSpace(conexao) ? this.ConnectionString : conexao,
            };
            this.conexao.Open();
            return this.conexao;
        }

        public void Dispose()
         {
            if(conexao != null)
                if (this.conexao.State == System.Data.ConnectionState.Open)
                    conexao.Close();
        }

        public IDbTransaction BeginTransaction()
        {
            return conexao.BeginTransaction();
        }

        public IDbTransaction BeginTransaction(IsolationLevel il)
        {
            throw new NotImplementedException();
        }

        public void ChangeDatabase(string databaseName)
        {
            throw new NotImplementedException();
        }

        public void Close()
        {
            if (conexao.State == ConnectionState.Open)
                conexao.Close();
        }

        public IDbCommand CreateCommand()
        {
            return this.conexao.CreateCommand();
        }

        public void Open()
        {
            this.conexao.Open();
        }
    }
}
