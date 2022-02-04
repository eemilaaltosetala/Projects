using System;
using System.Collections.Generic;
using System.Text;

namespace peli
{
    //Luokka Joukkue, toteuttaa rajapintaa IOsallistuja
    class Joukkue : IOsallistuja
    {
        //Automaattiset ominaisuudet, jotka toteuttavat rajapinnan
        public string Nimi { get; set; }
        public int Id { get; set; }
    }
}
