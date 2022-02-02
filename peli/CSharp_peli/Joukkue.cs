using System;
using System.Collections.Generic;
using System.Text;

namespace Tentti03
{
    //Luokka Joukkue, toteuttaa rajapintaa IOsallistuja
    class Joukkue : IOsallistuja
    {
        //Automaattiset ominaisuudet, jotka toteuttavat rajapinnan
        public string Nimi { get; set; }
        public int Id { get; set; }
    }
}