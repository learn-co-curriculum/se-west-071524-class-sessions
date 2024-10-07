import React, { useState } from "react";
import Pet from "./Pet";
import Filters from "./Filters";
import RotateLoader from "react-spinners/RotateLoader";
import { css } from "@emotion/react";
import { useSelector} from 'react-redux'

function PetBrowser() {

  const [type, setType] = useState("")


  

  return (
    <div>
      {/* <div className="ui cards">{petCards}</div> */}
    </div>
  );
}

export default PetBrowser;
