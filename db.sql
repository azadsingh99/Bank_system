--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bank; Type: TABLE; Schema: public; Owner: azad
--

CREATE TABLE public.bank (
    account integer NOT NULL,
    firstname character varying(20),
    lastname character varying(20),
    balance integer
);


ALTER TABLE public.bank OWNER TO azad;

--
-- Data for Name: bank; Type: TABLE DATA; Schema: public; Owner: azad
--

COPY public.bank (account, firstname, lastname, balance) FROM stdin;
101	Anand	Singh	6000
100	Azad	Singh	13000
\.


--
-- Name: bank bank_pkey; Type: CONSTRAINT; Schema: public; Owner: azad
--

ALTER TABLE ONLY public.bank
    ADD CONSTRAINT bank_pkey PRIMARY KEY (account);


--
-- PostgreSQL database dump complete
--

