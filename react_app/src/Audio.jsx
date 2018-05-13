import React from "react";
import styled from "styled-components";

const Wrapper = styled.div`
  display: flex;
  width: 10rem;
  height: 5rem;
  color: red;
  background-color: blue;
`;

const Audio = props => <Wrapper>{props.label}</Wrapper>;

export default Audio;
