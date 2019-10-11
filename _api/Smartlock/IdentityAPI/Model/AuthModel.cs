using System.Collections.Generic;

namespace IdentityAPI.Model
{
    public class AuthModel
    {
        public int UserId { get; set; }
        public string AccessKey { get; set; }
        public string Nome { get; set; }
        public IEnumerable<string> Digitais { get; set; }
    }
}
