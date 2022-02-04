using System;
using System.Collections.Generic;
using System.Text;

namespace peli
{
    //Luokka Suoritus, joka on geneerinen
    class Suoritus<TOsallistuja, TTulos>
    {
        //Ominaisuudet, geneerisiä
        public TOsallistuja Osallistuja { get; set; }
        public TTulos Tulos { get; set; }
    }
}
