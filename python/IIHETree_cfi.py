import FWCore.ParameterSet.Config as cms
import getpass, os
pwd = os.getcwd()
os.chdir("UserCode/IIHETree/")
username = getpass.getuser()
os.system("git log -n 1 | head -n 1 | awk '{print $2}' > /tmp/%s_git.hash"%username)
f = open('/tmp/git.hash')
git_hash = f.read().rstrip('\n')
print 'Using git hash: ' , git_hash
os.chdir(pwd)
IIHEAnalysis = cms.EDAnalyzer("IIHEAnalysis",
    debug         = cms.bool(True),
    beamSpot      = cms.InputTag("offlineBeamSpot"),
    primaryVertex = cms.InputTag('offlinePrimaryVertices'),
    git_hash = cms.string(git_hash),
    EcalHcal1EffAreaBarrel  = cms.untracked.double(0.28),
    EcalHcal1EffAreaEndcaps = cms.untracked.double(0.28),
    barrelEtaUpper_41 = cms.untracked.double( 1.442  ),
    endcapEtaLower_41 = cms.untracked.double( 1.56   ),
    endcapEtaUpper_41 = cms.untracked.double( 2.5    ),
    barrelEtaUpper_50 = cms.untracked.double( 1.4442 ),
    endcapEtaLower_50 = cms.untracked.double( 1.566  ),
    endcapEtaUpper_50 = cms.untracked.double( 2.5    ),
    isolEMHadDepth1ConstantTermBarrel_41       = cms.untracked.double( 2.0  ),
    isolEMHadDepth1ConstantTermEndcapLowEt_41  = cms.untracked.double( 2.5  ),
    isolEMHadDepth1ConstantTermEndcapHighEt_41 = cms.untracked.double( 2.5  ),
    isolEMHadDepth1LinearTermBarrel_41         = cms.untracked.double( 0.03 ),
    isolEMHadDepth1LinearTermEndcap_41         = cms.untracked.double( 0.03 ),
    isolEMHadDepth1OffsetTermEndcap_41         = cms.untracked.double( 50.0 ),
    isolEMHadDepth1ConstantTermBarrel_50_50ns       = cms.untracked.double( 2.0  ),
    isolEMHadDepth1ConstantTermEndcapLowEt_50_50ns  = cms.untracked.double( 2.5  ),
    isolEMHadDepth1ConstantTermEndcapHighEt_50_50ns = cms.untracked.double( 2.5  ),
    isolEMHadDepth1LinearTermBarrel_50_50ns         = cms.untracked.double( 0.03 ),
    isolEMHadDepth1LinearTermEndcap_50_50ns         = cms.untracked.double( 0.03 ),
    isolEMHadDepth1OffsetTermEndcap_50_50ns         = cms.untracked.double( 50.0 ),
    isolEMHadDepth1ConstantTermBarrel_50_25ns       = cms.untracked.double( 2.0  ),
    isolEMHadDepth1ConstantTermEndcapLowEt_50_25ns  = cms.untracked.double( 2.5  ),
    isolEMHadDepth1ConstantTermEndcapHighEt_50_25ns = cms.untracked.double( 2.5  ),
    isolEMHadDepth1LinearTermBarrel_50_25ns         = cms.untracked.double( 0.03 ),
    isolEMHadDepth1LinearTermEndcap_50_25ns         = cms.untracked.double( 0.03 ),
    isolEMHadDepth1OffsetTermEndcap_50_25ns         = cms.untracked.double( 50.0 ),
    EtThresholdBarrel_41 = cms.untracked.double( 35.0 ),
    EtThresholdEndcap_41 = cms.untracked.double( 35.0 ),
    EtThresholdBarrel_50 = cms.untracked.double( 35.0 ),
    EtThresholdEndcap_50 = cms.untracked.double( 35.0 ),
    dEtaInThresholdBarrel_41 = cms.untracked.double( 0.005 ),
    dEtaInThresholdEndcap_41 = cms.untracked.double( 0.007 ),
    dEtaInConstantTermBarrel_50_50ns = cms.untracked.double( 0.016  ),
    dEtaInLinearTermBarrel_50_50ns   = cms.untracked.double( 0.0001 ),
    dEtaInCutoffTermBarrel_50_50ns   = cms.untracked.double( 0.004  ),
    dEtaInThresholdEndcap_50_50ns    = cms.untracked.double( 0.02   ),
    dEtaInConstantTermBarrel_50_25ns = cms.untracked.double( 0.016  ),
    dEtaInLinearTermBarrel_50_25ns   = cms.untracked.double( 0.0001 ),
    dEtaInCutoffTermBarrel_50_25ns   = cms.untracked.double( 0.004  ),
    dEtaInConstantTermEndcap_50_25ns = cms.untracked.double( 0.016  ),
    dEtaInLinearTermEndcap_50_25ns   = cms.untracked.double( 0.0001 ),
    dEtaInCutoffTermEndcap_50_25ns   = cms.untracked.double( 0.004  ),
    dPhiInThresholdBarrel_41      = cms.untracked.double( 0.06 ),
    dPhiInThresholdEndcap_41      = cms.untracked.double( 0.06 ),
    dPhiInThresholdBarrel_50_50ns = cms.untracked.double( 0.06 ),
    dPhiInThresholdEndcap_50_50ns = cms.untracked.double( 0.15 ),
    dPhiInThresholdBarrel_50_25ns = cms.untracked.double( 0.06 ),
    dPhiInThresholdEndcap_50_25ns = cms.untracked.double( 0.06 ),
    HOverEThresholdBarrel_41 = cms.untracked.double( 0.05 ),
    HOverEThresholdEndcap_41 = cms.untracked.double( 0.05 ),
    HOverEReciprocalTermBarrel_50_50ns = cms.untracked.double(  2.0  ),
    HOverEConstantTermBarrel_50_50ns   = cms.untracked.double(  0.05 ),
    HOverEReciprocalTermEndcap_50_50ns = cms.untracked.double( 12.5  ),
    HOverEConstantTermEndcap_50_50ns   = cms.untracked.double(  0.05 ),
    HOverEReciprocalTermBarrel_50_25ns = cms.untracked.double(  2.0  ),
    HOverEConstantTermBarrel_50_25ns   = cms.untracked.double(  0.05 ),
    HOverEReciprocalTermEndcap_50_25ns = cms.untracked.double( 12.5  ),
    HOverEConstantTermEndcap_50_25ns   = cms.untracked.double(  0.05 ),
    SigmaIetaIetaThreshold_41      = cms.untracked.double( 0.03 ),
    SigmaIetaIetaThreshold_50_50ns = cms.untracked.double( 0.03 ),
    SigmaIetaIetaThreshold_50_25ns = cms.untracked.double( 0.03 ),
    E1x5threshold_41      = cms.untracked.double( 0.83 ),
    E2x5threshold_41      = cms.untracked.double( 0.94 ),
    E1x5threshold_50_50ns = cms.untracked.double( 0.83 ),
    E2x5threshold_50_50ns = cms.untracked.double( 0.94 ),
    E1x5threshold_50_25ns = cms.untracked.double( 0.83 ),
    E2x5threshold_50_25ns = cms.untracked.double( 0.94 ),
    IsolPtTrksThresholdBarrel_41      = cms.untracked.double( 5.0 ),
    IsolPtTrksThresholdEndcap_41      = cms.untracked.double( 5.0 ),
    IsolPtTrksThresholdBarrel_50_50ns = cms.untracked.double( 5.0 ),
    IsolPtTrksThresholdEndcap_50_50ns = cms.untracked.double( 5.0 ),
    IsolPtTrksThresholdBarrel_50_25ns = cms.untracked.double( 5.0 ),
    IsolPtTrksThresholdEndcap_50_25ns = cms.untracked.double( 5.0 ),
    dxyFirstPvThresholdBarrel_41      = cms.untracked.double( 0.02 ),
    dxyFirstPvThresholdEndcap_41      = cms.untracked.double( 0.05 ),
    dxyFirstPvThresholdBarrel_50_50ns = cms.untracked.double( 0.02 ),
    dxyFirstPvThresholdEndcap_50_50ns = cms.untracked.double( 0.05 ),
    dxyFirstPvThresholdBarrel_50_25ns = cms.untracked.double( 0.02 ),
    dxyFirstPvThresholdEndcap_50_25ns = cms.untracked.double( 0.05 ),
    missingHitsThreshold_41      = cms.untracked.double( 1 ),
    missingHitsThreshold_50_50ns = cms.untracked.double( 1 ),
    missingHitsThreshold_50_25ns = cms.untracked.double( 1 )
)
