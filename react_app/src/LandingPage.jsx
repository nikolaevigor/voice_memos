import React from "react";
import styled from "styled-components";
import { Grid } from "react-flexbox-grid";

const TextWrapper = styled.div`
  display: flex;
  flex-direction: column;
  background-color: yellow;
`;

const LandingPage = () => (
  <Grid>
    <TextWrapper />
  </Grid>
);

export default LandingPage;
