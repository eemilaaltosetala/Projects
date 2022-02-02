using System;
using System.Collections.Generic;
using System.Text;

namespace Tentti03
{
    //Luokka Kilpailu, joka on geneerinen
    class Kilpailu<TOsallisuja, TTulos>
    {
        //Ominaisuudet
        public string Nimi { get; set; }
        //Lista, geneerinen
        public List<Suoritus<TOsallisuja, TTulos>> Suoritukset { get; set; }

        //Konstruktori
        public Kilpailu()
        {
            //tehdään uusi lista
            Suoritukset = new List<Suoritus<TOsallisuja, TTulos>>();
        }
    }
}
