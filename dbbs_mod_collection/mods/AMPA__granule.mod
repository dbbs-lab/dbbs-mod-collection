TITLE 

COMMENT
ENDCOMMENT

NEURON {
    POINT_PROCESS glia__dbbs_mod_collection__AMPA__granule
    NONSPECIFIC_CURRENT i
    RANGE Q10_diff, Q10_channel
    RANGE R, g, ic, yuno
    RANGE Cdur, Erev
    RANGE r1FIX, r2, r3, r4, r5, gmax, r1, r6, r6FIX, kB
    RANGE tau_1, tau_rec, tau_facil, U
    RANGE PRE, T, Tmax
    RANGE diffuse, Trelease, lamd
    RANGE M, Diff, Rd, O
    RANGE tspike
    RANGE nd, syntype, gmax_factor
}

UNITS {
    (nA) = (nanoamp)
    (mV) = (millivolt)
    (umho) = (micromho)
    (mM) = (milli/liter)
    (pS) = (picosiemens)
    (nS) = (nanosiemens)
    (um) = (micrometer)
    PI = (pi) (1)
}

PARAMETER {
    syntype
    gmax_factor = 1
    Q10_diff = 1.5
    Q10_channel = 2.4
    gmax = 1200 (pS)
    U = 0.42 (1) <0,1>
    tau_rec = 8 (ms) <1e-9,1e9>
    tau_facil = 5 (ms) <0,1e9>
    M = 21.515
    Rd = 1.03 (um)
    Diff = 0.223 (um2/ms)
    Cdur = 0.3 (ms)
    r1FIX = 5.4 (/ms/mM)
    r2 = 0.82 (/ms)
    r3 = 0 (/ms)
    r4 = 0 (/ms)
    r5 = 0.013 (/ms)
    r6FIX = 1.12 (/ms/mM)
    Erev = 0 (mV)
    kB = 0.44 (mM)
    tau_1 = 1 (ms) <1e-9,1e9>
    u0 = 0 (1) <0,1>
    Tmax = 1 (mM)
    diffuse = 1
    lamd = 20 (nm)
    nd = 1
    celsius (degC)
}

ASSIGNED {
    v (mV)
    i (nA)
    ic (nA)
    g (pS)
    r1 (/ms)
    r6 (/ms)
    T (mM)
    Trelease (mM)
    tspike[100] (ms)
    x
    tsyn (ms)
    PRE[100]
    Mres (mM)
    numpulses
    tzero
    gbar_Q10 (mho/cm2)
    Q10 (1)
    yuno
}

STATE {
    C
    O
    D
}

INITIAL {
    C = 1
    O = 0
    D = 0
    T = 0(mM)
    yuno = 0
    numpulses = 0
    Trelease = 0(mM)
    tspike[0] = 1e12(ms)
    gbar_Q10 = Q10_diff^((celsius-30)/10)
    Q10 = Q10_channel^((celsius-30)/10)
    Mres = 1e3*(1e3*1e15/6.022e23*M)
    numpulses = 0
    FROM i = 1 TO 100 {
        PRE[i-1] = 0
        tspike[i-1] = 0
    }
    tspike[0] = 1e12(ms)
    IF (tau_1>=tau_rec) {
        printf("Warning: tau_1 (%g) should never be higher neither equal to tau_rec (%g)!\n", tau_1, tau_rec)
        tau_rec = tau_1+1e-5
    }
}

FUNCTION imax(a, b) {
    IF (a>b) {
        imax = a
    } ELSE {
        imax = b
    }
}

FUNCTION diffusione() {
    LOCAL DifWave, i, cntc, fi, aaa
    DifWave = 0
    cntc = imax(numpulses-100, 0)
    FROM i = cntc TO numpulses {
        fi = fmod(i, 100)
        tzero = tspike[fi]
        IF (t>tzero) {
            aaa = (-Rd*Rd/(4*Diff*(t-tzero)))
            IF (fabs(aaa)<699) {
                DifWave = DifWave+PRE[fi]*Mres*exp(aaa)/((4*PI*Diff*(1e-3)*lamd)*(t-tzero))
            } ELSE {
                IF (aaa>0) {
                    DifWave = DifWave+PRE[fi]*Mres*exp(699)/((4*PI*Diff*(1e-3)*lamd)*(t-tzero))
                } ELSE {
                    DifWave = DifWave+PRE[fi]*Mres*exp(-699)/((4*PI*Diff*(1e-3)*lamd)*(t-tzero))
                }
            }
        }
    }
    diffusione = DifWave
}

BREAKPOINT {
    IF (diffuse && (t>tspike[0])) {
        Trelease = T+diffusione()
    } ELSE {
        Trelease = T
    }
    SOLVE kstates METHOD sparse
    g = gmax*gbar_Q10*O
    i = (1e-6)*g*(v-Erev)*gmax_factor
    ic = i
}

KINETIC kstates {
    r1 = r1FIX*Trelease^2/(Trelease+kB)^2
    r6 = r6FIX*Trelease^2/(Trelease+kB)^2
    ~ C <-> O (r1*Q10, r2*Q10)
    ~ D <-> C (r5*Q10, r6*Q10)
    CONSERVE C+O+D = 1
}

NET_RECEIVE (weight, on, nspike, tzero(ms), y, z, u, tsyn(ms)) {
    LOCAL fi
    INITIAL {
        y = 0
        z = 0
        u = u0
        tsyn = t
        nspike = 1
    }
    IF (flag == 0) {
        nspike = nspike+1
        IF (!on) {
            tzero = t
            on = 1
            z = z*exp(-(t-tsyn)/(tau_rec))
            z = z+(y*(exp(-(t-tsyn)/tau_1)-exp(-(t-tsyn)/(tau_rec)))/((tau_1/(tau_rec))-1))
            y = y*exp(-(t-tsyn)/tau_1)
            x = 1-y-z
            IF (tau_facil>0) {
                u = u*exp(-(t-tsyn)/tau_facil)
                u = u+U*(1-u)
            } ELSE {
                u = U
            }
            y = y+x*u
            T = Tmax*y
            yuno = y
            fi = fmod(numpulses, 100)
            PRE[fi] = y
            tspike[fi] = t
            numpulses = numpulses+1
            tsyn = t
        }
        net_send(Cdur, nspike)
    }
    IF (flag == nspike) {
        tzero = t
        T = 0
        on = 0
    }
}
